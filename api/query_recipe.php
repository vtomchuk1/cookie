<?php



    $conn = new PDO("mysql:host=localhost;dbname=recipe", "recipe", "recipe");
    $sql = "SELECT * FROM full_list;";
    $result = $conn->query($sql);
    $d = array();
    while($row = $result->fetch()){

        $data = $row['list_prod'];
        $data_string = explode("\n", $data);

        foreach($data_string as $value){
            $data2str = explode(' ', $value);

            foreach ($data2str as $item) {

            }
            echo $data2str[count($data2str)-2];
        }


/*
        array_push($d, array(
            'id'            => $row['id'],
            'name'          => $row['name'],
            'category'      => $row['category'],
            'time_cookie'   => $row['time_cookie'],
            'time_eat'      => $row['time_eat'],
            'level'         => $row['level'],
            'list_prod'     => $row['list_prod'],
            'instruction'   => $row['instruction'],
            'image'         => $row['image'],));
*/
    }
    //echo var_dump($d);

?>
<p>hello world</p>
