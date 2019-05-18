# Religion2Vec
Religion2Vec provides a web interface to explore semantic analysis of words in the corpuses of the three main religious books: the Quran, the Bible, and the Torah.<br>

In order to use the interface, there are steps you need to follow:

1. Install `python` in case you have not already done so.
2. Create a new folder in the 'www' directory of your WampServer, and add all the files of the project to it.
3. Once you have your files ready, please edit the file `python-path.config` to where you have installed python, as this enables Wamp to locate python. For example,
edit the file into `C:\Users\...\AppData\Local\Programs\Python\Python37-32\python.exe`.
4. Make sure you have installed all the python libraries needed for running the script, specifically, the following libraries:
   * `gensim`
   * `pandas`
   * `json`

Once the requirements are met, launch the app by opening `page.html` on your Wamp host.
