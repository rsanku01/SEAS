import pandas

excel_data_df = pandas.read_excel("simulation_inputs.xlsx")

json_str = excel_data_df.to_json()
