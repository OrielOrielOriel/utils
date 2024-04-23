#!/usr/bin/python
import argparse
import os

CTF_ROOT = '/home/oriel/CTFs'
CTF_DIRECTORIES = ['.ctftool', 'scans', 'loot', 'exploits', '.meta']

def do_start():
    pass

def do_progress():
    pass

def parse_arguments():
  parser = argparse.ArgumentParser(
      prog='ctftool',
      description='Utility for managing CTF directories, access, and resources')
  
  subparsers = parser.add_subparsers()

  # CTF Start
  parser_start = subparsers.add_parser('start', aliases=['init', 's'], help='Start a new CTF')
  parser_start.add_argument('-n', '--name', type=str, help='Name of new CTF')

  # CTF Progress
  parser_progress = subparser.add_parser('progress', aliases=['prog', 'p'], help='Progress in a CTF')
  parser_progress.add_argument('-n', '--name', type=str, help='Name to assign to flag or credential')
  parser_progress.add_argument('-f', '--flag', type=str, help='Flag string')
  parser_progress.add_argument('-c', '--creds', type=str, help='Credential string or file to register')

  return parser.parse_args()

def create_ctf(ctf_name=str):
  root_path = os.path.join(CTF_ROOT, ctf_name)

  os.makedirs(root_path)
  print(f'Created CTF home directory: {root_path}')

  for d in CTF_DIRECTORIES:
    path = os.path.join(root_path, d)
    os.makedirs(path)

  print(f'Created CTF subdirectories: {CTF_DIRECTORIES}')
  

def main():
    arguments = parse_arguments()

    print(arguments)

if __name__ == '__main__':
    main()
