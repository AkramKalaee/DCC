from pathlib import Path
from argparse import ArgumentParser
import os

class LightWeightMethodArgParser:
    '''
        config class argument parser used solely for lightweight method.
    '''

    def __init__(self):
        self.parser = ArgumentParser(
            description='The parameters for the Lightweight Approach.')

        # default code_path is pointed to fashion mnist example. 
        self.parser.add_argument('-ipt', dest='code_path',
                                 default='../test/fashion_mnist', type=str,
                                 help='Path to the source code. Default: ../test/fashion_mnist')

        self.parser.add_argument('-opt', dest='output_types',
                                 metavar='N', type=int,
                                 nargs='+', choices={1, 2, 3, 4, 5},
                                 default={1},
                                 help='Types of output: 1 = call graph, 2 = call tress, 3 = RDF graphs, 4 = TensorFlow sequences, 5 = Extract triples.')
        self.parser.add_argument('--arg', dest='show_arg',
                                 action='store_true',
                                 help='Show arguments on graph')
        self.parser.set_defaults(Pshow_arg=False)
        self.parser.add_argument('--url', dest='show_url',
                                 action='store_true',
                                 help='Show url on graph')
        self.parser.set_defaults(show_url=False)

    def get_args(self, args):
        return self.parser.parse_args(args)


class LightWeightMethodConfig:
    '''
        config class controllable in lightweight method.
    '''

    def __init__(self, arg):
        self.code_path = Path(arg.code_path)
        self.code_path = self.code_path.resolve()
        self.output_types = arg.output_types
        self.show_arg = arg.show_arg
        self.show_url = arg.show_url


class GenerateSummaryArgParser:
    '''
        Argument Parser for script to generate summary file.
    '''

    def __init__(self):
        self.parser = ArgumentParser(
            description='The parameters for script to generate summary file.')
        self.parser.add_argument('-p', '--path',
                                 type=str,
                                 help="Path to code directory.")

    def get_args(self):
        return self.parser.parse_args()


class GraphHandlerArgParser:
    '''
        Argument Parser for GraphHandler.
    '''

    def __init__(self):
        self.parser = ArgumentParser(
            description="The parameters for tf.graph handler.")
        default_path = Path(".")
        default_path = default_path.resolve()

        self.parser.add_argument('-ld', '--logdir',
                                 default=default_path,
                                 type=str,
                                 help='directory for saved graph')

    def get_args(self):
        return self.parser.parse_args()


class PaperswithcodeArgParser:
    '''
        Argument Parser for Paperswithcode script
    '''

    def __init__(self):
        self.parser = ArgumentParser(
            description="The parameters for Paperswithcode script.")
        default_path = Path("../")/"core"/"chromedriver"
        default_path = default_path.resolve()
        self.parser.add_argument('-cd', '--chromedriver',
                                 default=default_path,
                                 type=str,
                                 help="Path to chromedirver.")
        self.parser.add_argument('-url',
                                 default="https://paperswithcode.com/latest",
                                 type=str,
                                 help="URL to Paperswithcode website")
        self.parser.add_argument('-limit',
                                 default=-1,
                                 type=int,
                                 help="Number of paper/code to download.")

    def get_args(self):
        return self.parser.parse_args()