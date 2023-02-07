<?php

try {

    $id = $_POST['id'];
    $conn = new PDO("mysql:host=localhost;dbname=recipe", "recipe", "recipe");
    $sql = "SELECT * FROM full_list WHERE id = {$id};";
    $result = $conn->query($sql);
    $d = array();
    while($row = $result->fetch()){
        array_push($d, array(
            'id'            => $row['id'],
            'name'          => $row['name'],
            'category'      => $row['category'],
            'time_cookie'   => $row['time_cookie'],
            'list_prod'     => $row['list_prod'],
            'instruction'   => $row['instruction']));
    }
    echo json_encode($d,JSON_UNESCAPED_UNICODE  );
}
catch (PDOException $e) {
    echo "Database error: " . $e->getMessage();
}

?>
