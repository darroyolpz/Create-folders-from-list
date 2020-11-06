import os
import pandas as pd

# Open file with the orders to be created
excel_file = 'AHU Orders.xlsx'
df = pd.read_excel(excel_file)
df['Orders'] = df['Orders'].astype(str)

# Loop and create the folders
for order in df['Orders']:
	# Nested subfolders to be created
	subfolders = ['DVF', 'Control & wiring diagrams']

	try:
		for subfolder in subfolders:
			folder_to_create = order + '/' + subfolder

			# Create new folder in the path where the script is located
			os.makedirs(folder_to_create)
			print('Folder', folder_to_create, 'created')
		print('\n')
	except:
		print('Warning! Folder', folder_to_create, 'already created')
		print('\n')
