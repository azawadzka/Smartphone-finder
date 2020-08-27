# https://clipspy.readthedocs.io/

import clips
import pickle
import pandas as pd

path_to_data_clean_pickle = 'Projects\smartphones\\application\data_clean.pickle'
path_to_smartphones_clp = 'Projects\smartphones\\application\\filtering_rules.clp'

class DataBase:

    def __init__(self):
        self.smartphones = None
        with open(path_to_data_clean_pickle, 'rb') as handle:
            self.smartphones = pickle.load(handle)  # pandas DataFrame

        self.columns = self.smartphones.columns
        self.env = clips.Environment()
        self.env.load(path_to_smartphones_clp)
        self.env.reset()
        self.fill_database()

    def run(self):
        self.env.run()

    def reset(self):
        self.env.reset()
        self.fill_database()

    def fill_database(self):
        template_smartphone = self.env.find_template('smartphone')
        for idx, smartphone in self.smartphones.iterrows():
            fact = template_smartphone.new_fact()
            fact['id'] = clips.Symbol(str(idx))
            fact['valid'] = clips.Symbol("true")
            for key, value in smartphone.iteritems():
                if value is not None:
                    if isinstance(value, float) or isinstance(value, int):
                        fact[key] = value
                    else:
                        fact[key] = clips.Symbol(str(value))
                else:
                    fact[key] = clips.Symbol('unknown')  # needs any value to be excluded when searching
            fact.assertit()

    def test(self):
        template_op_s_request = self.env.find_template('request_operating_system')
        fact = template_op_s_request.new_fact()
        fact['multivalue'] = [clips.Symbol('Android')]
        fact.assertit()

    def put_request_quantitative(self, template_name, value, operation):
        template = self.env.find_template(template_name)
        fact = template.new_fact()
        fact['value'] = value
        fact['operation'] = clips.Symbol(str(operation))
        fact.assertit()

    def put_request_multivalue(self, template_name, list_of_values):
        # pass list to multislot
        template = self.env.find_template(template_name)
        fact = template.new_fact()
        fact['multivalue'] = [clips.Symbol(str(i)) for i in list_of_values]
        fact.assertit()

    # not working
    def put_request_binary(self, template_name, value):
        template = self.env.find_template(template_name)
        fact = template.new_fact()
        fact['has'] = clips.Symbol(str(value))
        fact.assertit()








