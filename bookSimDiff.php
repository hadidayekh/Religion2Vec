<?php
	
	function getSimilarWords($book, $word, $sim, $word2){
		$python = "C:\\Users\\tce\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe";
		$command = "$python bookSimDiff.py " . $book. ' ' .$word. ' ' . $sim . ' ' . $word2.' 5';
		$output = shell_exec($command);
		return $output;
	}
	
	if (isset($_GET['book'])) {
		$book = $_GET['book'];
	}
	if (isset($_GET['word'])) {
		$word = $_GET['word'];
	}
	
	if (isset($_GET['sim'])) {
		$sim = $_GET['sim'];
	}
	
	if (isset($_GET['word2'])) {
		$word2 = $_GET['word2'];
	}
	
	if (isset($_GET['word']) && isset($_GET['sim']) && isset($_GET['word2'])){
		$output = getSimilarWords($book, $word, $sim, $word2);
		echo $output;
	}
	
		
?>