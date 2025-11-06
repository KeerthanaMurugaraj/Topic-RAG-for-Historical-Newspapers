import argparse
import os.path

import pandas
import googletrans
from langdetect import detect
import swifter
import time


def detect_language(text):
    try:
        return detect(text)
    except:
        return 'unknown'


def google_translate(text, source='auto', target='en'):
    detected_language = None
    translated_text = None
    iter = 0
    while not (detected_language == "en" or detected_language == "unknown") and iter <= 5:
        translator = googletrans.Translator()
        translated_text = translator.translate(str(text), dest=target, src=source).text
        detected_language = detect_language(translated_text)
        iter += 1
        if iter == 5:
            print(f"Language translation failed for text: {str(text)}.")
    return translated_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--first_row', type=int, help='first row to translate')
    parser.add_argument('-l', '--last_row', type=int, help='last row to translate')
    parser.add_argument('-i', '--input_pkl_file', type=str, help='input pickle file')
    parser.add_argument('-o', '--output_directory', type=str, help='output directory')
    parser.add_argument('-t', '--list_columns', type=str, help='list of columns to translate with separator ,')
    args = parser.parse_args()
    start_time = time.perf_counter()
    print(' '.join(f'{k}={v}' for k, v in vars(args).items()))
    ip_df = pandas.read_pickle(args.input_pkl_file)[args.first_row:args.last_row]
    translate_columns = [str(item).strip() for item in args.list_columns.split(',')]
    print(f"length of input data: {len(ip_df)}, with first row: {args.first_row}, with last row: {args.last_row}")
    for translate_column in translate_columns:
        ip_df[translate_column + "_translated"] = ip_df[translate_column].swifter.apply(lambda row: google_translate(row))
    ip_df.to_pickle(os.path.join(args.output_directory, os.path.basename(
        os.path.realpath(args.input_pkl_file).split(".pkl")[0] + "_" + str(args.first_row) + "_" + str(
            args.last_row) + ".pkl")))
    # ip_df.to_csv(os.path.join(args.output_directory, os.path.basename(
    #     os.path.realpath(args.input_pkl_file).split(".pkl")[0] + "_" + str(args.first_row) + "_" + str(
    #         args.last_row) + ".csv")))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'File translation completed successfully in {total_time:.4f} seconds')
