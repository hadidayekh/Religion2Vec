<?php
	$nb = '5';
	$nbint = 5;

	function getSimilarWords($modelfile, $picklefile, $word, $nb, $type){
		//$python = "C:\\Users\\tce\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe";
		$python = trim(file_get_contents('../config/python-path.config'));
		$command = "$python book2vec.py ".$modelfile. ' ' . $picklefile. ' '. $word. ' ' . $nb . ' ' . $type;
		//$output = exec($command);
		return $command;
	}
	if (isset($_GET['modelfile'])) {
		$modelfile = $_GET['modelfile'];
	}
	if (isset($_GET['picklefile'])) {
		$picklefile = $_GET['picklefile'];
	}
	
	if (isset($_GET['word'])) {
		$word = $_GET['word'];
	}
	
	if (isset($_GET['similarnb'])) {
		$nb = $_GET['similarnb'];
		
		if($nb==''){
			$nb = '5';
		}
		$nbint = intval($nb);
	}
	
	if (isset($_GET['wordType'])) {
		$type = $_GET['wordType'];
		$type = strtolower($type);
		if (trim($type) == 'part of speech'){
			$type ='any';
		}
		
	}
	
	if (isset($_GET['word']) && isset($_GET['wordType']) && isset($_GET['similarnb'])){
		
		if($word != ""){
			$output = getSimilarWords($modelfile, $picklefile, $word, $nb, $type);
			if(trim($output) =='absent'){
				echo "absent";
			}else{
				echo $output;
			}
		}
	}	
?>