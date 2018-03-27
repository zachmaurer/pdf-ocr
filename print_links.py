import pandas as pd
from collections import defaultdict
import pickle

SUBMISSION_CSV = 'scores.csv'
TITLES_DICT = 'titles_dict.pkl'

def printLinks():
  # Load Names to Submissions
  df = pd.read_csv(SUBMISSION_CSV)[['Name', 'Submission ID']]
  submission_to_names = defaultdict(list)
  for index, row in df.iterrows():
    try:  
      name, sid = row['Name'], int(row['Submission ID'])
    except:
      continue
    submission_to_names[sid].append(name)

  # Load Titles To Submissions
  submission_to_title = pickle.load(open(TITLES_DICT, 'rb'))

  num_missing = len(set(submission_to_title.keys()).symmetric_difference(set(submission_to_names.keys())))
  print("Number of missing records: {}".format(num_missing))

  # Start printing
  template = '<tr><td><a href="reports/{}.pdf">{}</a></td><td>{}</td></tr>' # id, title, names

  # Print
  for sid, title in submission_to_title.items():
    names = ', '.join(submission_to_names[int(sid)])
    print(template.format(sid, title, names))

def main():
  printLinks()

if __name__ == '__main__':
  main()