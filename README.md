# Create a PDF of the Practical Typography web book

[Butterick’s Practical Typography](https://practicaltypography.com/) is a fantastic web book about typography written in a charming style and equally no-nonsense attitude. Check it out!

It doesn't come as PDF, only as a collection of truly beautiful web pages. However having PDF is handy in a lot of situations (offline reading, printing, etc). So I put some scripts together to create a PDF all the web pages. The result us far from perfect (see TODO.md), but serves my reading well: 

Via the PDF I already have read - and truly enjoyed - ca. 30% of the book. **This is much more than I *ever* would have read via the web pages!**

### Note

Please beware, that Matthew Butterick consciously does [not provides a PDF version](https://practicaltypography.com/why-theres-no-e-book-or-pdf.html). Also please note that [the book is copyrighted](https://practicaltypography.com/end-credits.html#legal) and not to be reproduced. I understand that creating a PDF copy *for personal use* qualifies as fair use.

## Requirements

* [Python3](https://www.python.org/) with [Pipenv](https://docs.pipenv.org/) - *to download/prepare the HTML files*
* macOS with Safari - *to convert the HTML files to PDFs (via the print function)*
* Installed macOS Print Service "Save to Web Receipts Folder"
* [Keyboard Maestro](https://www.keyboardmaestro.com/main/) - *to automate the Safari printing for command line use*
* [QPDF](http://qpdf.sourceforge.net/) - *to combine the PDFs into one*

## Install

1) Make sure all the requirements are installed. (Python and QPDF can be installed via Homebrew, Pipenv can be installed via `pip`)
2) Add the Keyboard Maestro macro "SafariPrint" to your Keyboard Maestro instance (keep the name as is, so that it can be called under this name via Applescript.

## How to run

Firstly, make sure the Web Receipts folder `~/Documents/Web Receipts/` is empty. Then issue in the project directory:

    ./main.sh

and wait for ca. 1 hour. Afterwards the file `PracticalTypography.pdf` should contain a nice version of Butterick’s Practical Typography. - Voila!

## Credit

Firstly, of course, to **Matthew Butterick**, the author of Practical Typography, for writing and web publsihing this great read. And secondly to all the authors of the bits in the tool chain.

<!--  LocalWords:  Butterick QPDF Pipenv
 -->
