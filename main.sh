PDFDIR="PDFs"
OUTFILE="PracticalTypography.pdf"
OUTTEMP="Practical_temp.pdf"
PDFLISTFILE="pdf_list.txt"

echo "--- Run create_html_files.py"
pipenv install
pipenv run python ./create_html_files.py
echo

echo "--- Run print_in_safari.sh over clean_html_files.txt"
while read f; do echo "print $f"; ./print_in_safari.sh "$f"; done <clean_html_files.txt
echo

echo "--- Move the PDFs"
echo "wait..."; sleep 5 # wait for the file to arrive in the Web Recipts folder
mv -v ~/"Documents/Web Receipts/" $PDFDIR

echo "--- Make and move starting PDF to '$OUTFILE'"
./print_in_safari.sh 'https://practicaltypography.com/'
echo "wait..."; sleep 5 # wait for the file to arrive in the Web Receipts folder
mv -v ~/"Documents/Web Receipts"/* "$OUTFILE" || exit 9
qpdf "$OUTFILE" --pages "$OUTFILE" 1 -- "$OUTTEMP"
mv "$OUTTEMP" "$OUTFILE"


echo "--- Make list PDF list and run qpdf over it"
ls -tr "$PDFDIR"/* > "$PDFLISTFILE"
while read f; do    
    echo "adding $f"
    qpdf "$OUTFILE" --pages "$OUTFILE" "$f" -- "$OUTTEMP"
    mv "$OUTTEMP" "$OUTFILE"
done <  "$PDFLISTFILE"
