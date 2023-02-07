<?php

try {
    
    if(isset($_POST['id'])){
        $id = $_POST['id'];
        $sql = "SELECT * FROM full_list WHERE id = {$id};";
    }
    else if(isset($_POST['level'])){
        $level = $_POST['level'];
        $sql = "SELECT * FROM full_list WHERE level = '{$level}';";
    }
    else if(isset($_POST['category'])){
        $category = $_POST['category'];
        $sql = "SELECT * FROM full_list WHERE category = '{$category}';";
    }
    else{
        $sql = "SELECT * FROM full_list;";
    }
    $result = $conn->query($sql);
    $d = array();
    while($row = $result->fetch()){
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
    }
    echo json_encode($d,JSON_UNESCAPED_UNICODE  );
}
catch (PDOException $e) {
    echo "Database error: " . $e->getMessage();
}

?>