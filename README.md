# Religion2Vec
Religion2Vec provides a web interface to explore semantic analysis of words in the corpuses of the three main religious books: the Quran, the Bible, and the Torah.<br>

In order to use the interface, there are steps you need to follow:

1. Install `python` in case you have not done so already.
2. Make sure you have installed all the python libraries needed for running the script, specifically, the following libraries:
   * `gensim`
   * `pandas`
   * `json`
3. Install and set up WampServer in case you have not done so already.
4. Create a new folder in the 'www' directory of your WampServer, and add all the files of the project to it.
5. Once you have your files ready, edit the file `python-path.config` to where you have installed python, as this enables Wamp to locate python. For example,
edit the file into `C:\Users\...\AppData\Local\Programs\Python\Python37-32\python.exe`.

Now that all requirements are met, launch the app by opening `page.html` on your Wamp host.
