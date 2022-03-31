import pandas as pd
import os

from config import Config
from descriptor_processes.text_pre_process import pre_process
from evaluators.perfect_evaluator import PerfectEvaluator
from server.query_util import MigrationInfo

log_path = '/Users/usiusi/Documents/Report/Test-Reuse/Reports/report22/qlogs'
logs = []

config = Config()

top_scored_q =  pd.read_csv('dd.csv').fillna('')
#%%

cleaning_columns = ['target_text', 'target_content_desc', 'target_id']
ground_truth = pd.read_csv(config.ground_truth)
ground_truth.loc[:, cleaning_columns] = pre_process(ground_truth.loc[:, cleaning_columns], False)

count = 0
for index, row in top_scored_q.iterrows():
    mig_info = MigrationInfo.set_info_from_log(row)
    count+=PerfectEvaluator.event_exist_in_gt(row, mig_info)
print(count)
