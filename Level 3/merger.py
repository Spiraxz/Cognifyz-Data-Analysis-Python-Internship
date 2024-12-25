import sys
import nbformat

def merge_notebooks(file_list, output_file):
    merged_notebook = nbformat.v4.new_notebook()
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
            merged_notebook.cells.extend(nb.cells)
    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(merged_notebook, f)

if __name__ == "__main__":
    files_to_merge = sys.argv[1:-1]  # All but the last argument
    output_file = sys.argv[-1]      # Last argument
    merge_notebooks(["1p2.ipynb","L3.ipynb"], "Final.ipynb")
