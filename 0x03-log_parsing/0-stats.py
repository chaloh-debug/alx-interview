#!/usr/bin/python3
""" Log parsing """
import re


def extract_data(line):
    """ Extracts data from a log line """
    exps = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(exps[0], exps[1],
                                         exps[2], exps[3], exps[4])
    data_match = re.fullmatch(log_fmt, line)
    if data_match is not None:
        status_code = data_match.group('status_code')
        file_size = int(data_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    # print(info)
    return info


def print_stats(file_size, status_codes):
    """ Prints the stats """
    print('File size: {:d}'.format(file_size), flush=True)
    for status_code in sorted(status_codes.keys()):
        num = status_codes.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_stats(line, file_size, status_codes):
    """ Updates the stats """
    line_info = extract_data(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes.keys():
        status_codes[status_code] += 1
    return file_size + line_info['file_size']


def run():
    """ Starts the log parser. """
    line_num = 0
    file_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            file_size = update_stats(
                line,
                file_size,
                status_codes,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_stats(file_size, status_codes)
    except (KeyboardInterrupt, EOFError):
        print_stats(file_size, status_codes)


if __name__ == '__main__':
    run()
