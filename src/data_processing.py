# Functions for data loading and preprocessing
import os
import re
import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df


def clean_data(df):
    # Implement data cleaning steps
    return df_cleaned


def load_emoji_sentiment_data():
    filepath = os.path.join('data', 'raw', 'emoji_data', 'Emoji_Sentiment_Data_v1.0.csv')
    df = pd.read_csv(filepath)
    return df

def parse_emoji_test(file_path):
    """
    Parses the emoji-test.txt file and returns a DataFrame with emoji data.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    data = []
    group = ''
    subgroup = ''
    
    for line in lines:
        line = line.strip()
        if line.startswith('# group:'):
            group = line[8:].strip()
        elif line.startswith('# subgroup:'):
            subgroup = line[11:].strip()
        elif line and not line.startswith('#'):
            # Split the line into codepoints and description
            parts = line.split(';')
            codepoints = parts[0].strip()
            status_description = parts[1].split('#')
            status = status_description[0].strip()
            description = status_description[1].strip()
            emoji = description.split(' ')[0]
            name = ' '.join(description.split(' ')[1:])
            data.append({
                'group': group,
                'subgroup': subgroup,
                'codepoints': codepoints,
                'status': status,
                'emoji': emoji,
                'name': name
            })
    
    df = pd.DataFrame(data)
    return df
