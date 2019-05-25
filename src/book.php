<?php
	$nb = '5';
	$nbint = 5;

	function getSimilarWords($word, $nb, $type){
		//$python = "C:\\Users\\tce\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe";
		$python = trim(file_get_contents('../config/python-path.config'));
		$command = "$python book2vec.py ". $word. ' ' . $nb . ' ' . $type;
		$output = exec($command);
		return $output;
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
			$output = getSimilarWords($word, $nb, $type);
			if(trim($output) =='absent'){
				echo "absent";
			}
			else if (trim($output) =='') {
				echo "fail";
			}
			else{
				echo $output;
			}
		}
	}	
?>