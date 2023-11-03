% Define the file path to your CSV file
file_path = '/Users/lachlanbest/Documents/METR4911/Datasets/LSE_eSaude_UVIGO Labels/train_labels.csv';

% Read the CSV file into a table without variable names
data = readtable(file_path, 'Delimiter', ',', 'ReadVariableNames', false);

% Extract the data
train_file_name = data.Var1;  % Cell array of filenames
train_label = double(data.Var2);  % Numeric array of label values

% Convert each row entry in 'filenames' to a 1x1 cell containing a string
train_file_name = cell(size(data, 1), 1);  % Initialize a cell array

for i = 1:size(data, 1)
    train_file_name{i} = {char(data.Var1(i))};  % Convert each entry to a 1x1 cell
end