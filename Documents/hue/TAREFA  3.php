<?php
$grid=array(1,2,3,4,5);
$car_s=array(1,2,3,4,5);
$car_c=array(5,3,2,1,4);
$num_car=count($car_s);

$vc=array_combine($car_s,$grid);
$vf=array_combine($car_c,$grid);

$p=array();
$positivos=array();
for($i=1;$i<=$num_car;$i++){
	$p[$i]=$vc[$i]-$vf[$i];
}

if(in_array("0",$p)){
	for($x=1;$x<=$num_car;$x++){
		if($p[$x] == "0"){
			$kk=$vf[$x];
			for($t=1;$t<=$num_car;$t++){
				if($kk>$vc[$t] AND $kk<$vf[$t]){
					$um="1";
					$p[$x]=$um;
					echo "dento";
					print_r($p);
				}
			}
		}
	}
}
$num_f=array();
$positivos=array_values($p);
$q_posi=count($positivos);
for($tt=0;$tt<$q_posi;$tt++){
	if($positivos[$tt]<0){
		$positivos[$tt]=$positivos[$tt]-$positivos[$tt];
		
	}
}
$m_ultrapassagens=array_sum($positivos);
echo "o minimo de ultrapassagens eh:".$m_ultrapassagens;
?>
    
    
    
    