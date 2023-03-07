import lib.opensearch as opensearch
import lib.curator as curator
from lib.opensearch import OpensearchClient
import pydash as _
import yaml
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='Opensearch Curator.')
    parser.add_argument('-c', '--config',required=True)
    parser.add_argument('-d', '--dry-run',required=False, action='store_true')
    parser.add_argument('action_path', metavar='action_file_path', help='an integer for the accumulator')
    return parser

parser = get_parser()
args = parser.parse_args()
config_path = args.config
dry_run = args.dry_run
action_path = args.action_path
print(config_path)

options = {}
options['dry_run'] = dry_run

with open("/etc/curator/config.yml", "r") as stream:
    try:
        client_info = _.get(yaml.safe_load(stream), 'client')
        # print(client_info)
    except yaml.YAMLError as exc:
        print(exc)

opensearch = OpensearchClient(client_info)

# try:
#     opensearch.create_index('bob-2022.03.01')
#     opensearch.create_index('test-2022.03.02')
#     opensearch.create_index('test-2023.02.17')
#     # opensearch.create_index('test-2023.03.04')
#     # opensearch.create_index('test-2023.03.05')
# except:
#     print("Index exist")


with open(action_path, "r") as stream:
    try:
        actions = yaml.safe_load(stream)
        for action_list in actions['actions']:
            curator.do_curator_action(opensearch.list_index(), actions['actions'][action_list], options)
    except yaml.YAMLError as exc:
        print(exc)