import tabula

# Read PDF into list of DataFrame
dataframe = tabula.read_pdf("Report_20201009000009646.pdf", pages='all')

# Read remote PDF into list of DataFrame
dataframe_2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")

# Convert PDF into CSV file
data =tabula.convert_into("Report_20201009000009646.pdf", "output.csv", output_format="csv", pages='all')