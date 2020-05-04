from src.json_generation.data_preprocessing import DataPrepro
from src.json_generation.prepare_data import prepare_data
from src.json_generation.ent_sum_preprocessing import *
from src.utils import *
from src.flexible_models.flexible_sum import FlexibleSum, SummarizerModel

# Populate the cash metadata first - CAREFUL: LONG OPERATION
# cache = get_metadata_cache()
# cache.populate()

# Extract a book (text and metadata) 
create_file = DataPrepro()
create_file.create_json(b_id=788)

# Create genre tag
create_file.leave_one_genre()
create_file.stats_genre()

# Apply NER and split data into paragraphs
prepare_data(files=['788'], do_ner=True, do_split=True, verbose=1)

# Define summarizers to be used
summarizers_models = [SummarizerModel.PYSUM, SummarizerModel.KW, SummarizerModel.BART, SummarizerModel.T5]
summaries = ['PYSUM', 'KW', 'BART', 'T5']

# Perform summarization on each paragraph for all books (latest data format)
# Results are stored in different folders to optimise computations, since BART and T5 could be a bit long to compute
for summarizer_model, OUTPUT_DATA_FOLDER in zip(summarizers_models, OUTPUT_DATA_FOLDERS):
	book_ids = retrieve_list_of_books_to_summarize(PREPROC_PATH, OUTPUT_DATA_FOLDER, summarizer_model)
	apply_summarization(PREPROC_PATH, OUTPUT_DATA_FOLDER, book_ids, summarizer_model, batch_size=1)

# Merge selected summaries in the preproc data folder
merge_summaries(PREPROC_PATH, summaries)


"""
# Split into paragraphs
paragraph_preprocessing.separate_paragraphs_all_files(overwrite=False)
parser = paragraph_preprocessing.ParagraphParser(min_threshold=20, min_length=600, max_length=900)
paragraph_preprocessing.separate_in_paragraphs(parser, d_id='1342')

# Create ent_sum template
ent_sum_preprocessing.prepare_json_templates(True)

# Perform NER
model = FlexibleBERTNER(BERT_NER_LARGE, batch_size=128, max_length=2000)
ent_sum_preprocessing.perform_ner_on_file(model)
ent_sum_preprocessing.perform_ner_on_file(model, d_id= '1342')
"""
