
function drawGraph(result, chartName, book, wordType) {
			var wt = wordType;
			if (wt == 'any' || wt == 'part of speech') {
				wt = 'word';
			}
			var chartJson = {
				chart: {
					type: 'scatter',
					zoomType: 'xy'
				},
				title: {
					text: book
				},
				subtitle: {
					text: 'Showing the most similar '+wt+'s to <b>' + word + '</b>'
				},
				xAxis: {
					title: {
						enabled: true,
						text: 'x'
					},
					startOnTick: true,
					endOnTick: true,
					showLastLabel: true
				},
				yAxis: {
					title: {
						text: 'y'
					}
				},
				plotOptions: {
					scatter: {
						marker: {
							radius: 5,
							states: {
								hover: {
									enabled: true,
									lineColor: 'rgb(100,100,100)'
								}
							}
						},
						states: {
							hover: {
								marker: {
									enabled: false
								}
							}
						},
						tooltip: {
							headerFormat: '<b>{series.name}</b><br>',
							pointFormat: '<i>similarity:   </i>{point.sim_score}<br><i>word count:   </i>{point.word_count}'
						},
						dataLabels: {
							format: "{point.name}",
							enabled: true
						},
					}
				},
				series: [{
					name: word,
					marker: {
						symbol: 'circle'
					},
					color: 'rgba(0, 0, 83, 1)',
					data: [{
						name: word,
						x: result[similarnb]['x'],
						y: result[similarnb]['y'],
						x_rounded: round(result[similarnb]['x'], 2),
						y_rounded: round(result[similarnb]['y'], 2),
						sim_score: 1.0,
						word_count: result[similarnb]['word_count']
					}]
				}],
				navigation: {
					menuStyle: {
						border: '1px solid #A0A0A0',
						background: '#FFFFFF',
						padding: '5px 0'
					},
					menuItemStyle: {
						padding: '0 10px',
						background: null,
						color: '#303030',
						fontSize: '16px'
					}
				},
				exporting: {
					menuItemDefinitions: {
						remove: {
						  onclick: function() {
								var x = document.getElementById(chartName);
								x.parentNode.removeChild(x);
								removeId(book, word, wordType);
								if (book.toLowerCase() == "bible") {
									for (var i = 0; i < 3; i++) {
										if (biblecharts[i]) {
											biblecharts[i] = false;
											
											break;
										}
									}
								} else if (book.toLowerCase() == "torah") {
									for (var i = 0; i < 3; i++) {
										if (torahcharts[i]) {
											torahcharts[i] = false;
											break;
										}
									}
								} else {
									for (var i = 0; i < 3; i++) {
										if (qurancharts[i]) {
											qurancharts[i] = false;
											break;
										}
									}

								}
							},
						  text: "Remove"
						}
						
						
					},
					buttons: {
						contextButton: {
							menuItems: ["viewFullscreen", "printChart", "separator", "downloadPNG", "downloadJPEG", "downloadPDF", "downloadSVG", "remove"]
						}
						
					}
				}
			};
			var w;
			var x;
			var y;
			var s;
			for (var i = 0; i < similarnb; i++) {
				w = result[i]['word'];
				x = result[i]['x'];
				y = result[i]['y'];
				s = result[i]['sim_score'];
				count = result[i]['word_count'];
				chartJson.series[i + 1] = {
					name: w,
					marker: {
						symbol: 'circle'
					},
					color: 'rgba(223, 83, 83, .5)',
					data: [{
						name: w,
						x: x,
						y: y,
						x_rounded: round(x, 2),
						y_rounded: round(y, 2),
						sim_score: s,
						word_count: count
					}]
				};
			}
			if (similarnb > 15) {
				for (var i = 0; i <= similarnb; i++)
					chartJson.series[i]['showInLegend'] = false;
			}
			Highcharts.chart(chartName, chartJson);
		}		
		