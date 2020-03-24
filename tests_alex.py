
##########################################
# ALEX's TEST FILE, PLEASE DO NOT MODIFY #
##########################################

from importlib import reload
from src.json_generation import paragraph_preprocessing
from src.json_generation import ent_sum_preprocessing
from src.flexible_models import FlexibleBERTNER
from src.utils import *
# reload(paragraph_preprocessing)

# Split into paragraphs
paragraph_preprocessing.separate_paragraphs_all_files(overwrite=False)

# Perform NER
model = FlexibleBERTNER(BERT_NER_LARGE, batch_size=128, max_length=2000)
ent_sum_preprocessing.perform_ner_on_all(model)

