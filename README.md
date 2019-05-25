# Religion2Vec
Religion2Vec provides a web interface to explore semantic analysis of words in the corpuses of the three main religious books: the Quran, the Bible, and the Torah.<br>

### This branch will contain a tool to visualize any trained Word2Vec model. It currently contains a tool for analyzing the Bible ONLY. For the religious books case study, please refer to the Religion2Vec branch.

In order to use the interface, there are steps you need to follow:
#### Setting up the software:
1. Install `python` in case you have not done so already.
2. Make sure you have installed all the python libraries needed for running the script, specifically, the following libraries:
   * `gensim`
   * `pandas`
   * `json`
   * `sklearn`
3. Install and set up WampServer in case you have not done so already.
4. Create a new folder in the 'www' directory of your WampServer, and add all the files of the project to it.
5. Once you have your files ready, edit the file `python-path.config`, which is located in `config/`, to where you have installed python. This enables Wamp to locate python. For example,
edit the file into `C:\Users\...\AppData\Local\Programs\Python\Python37-32\python.exe`.

#### Performing dimensionality reduction:
The steps below need to be followed every time you want to explore a different model:
1. Locate your w2v file, which is your trained Word2Vec model.
2. Open `cmd` or `terminal` and <b>change the directory to the directory of the project</b>. Changing the directory is crucial, as the files will save in a relative path, and the software is reading from a relative path.
3. Run the following command, replacing the argument with the path to your w2v file:
   <pre><code>python w2v_tsne.py &ltpath-to-w2v-file&gt</code></pre>
4. Once the code finishes executing, the model and coordinates files will be saved in a `data` subfolder. Consider <b>saving</b> these in a different folder for future use. Make sure that if you want to explore a specific model, you add the corresponding files to the `data` subfolder with the names `book2vec.w2v` and `reduced_book.pkl`.
<br>
Now that all requirements are met, launch the app by opening the folder you created it on your Wamp host.
