from sqlGenerator.queryGenerator import queryGenerator

base = """
    <?php
    include_once("../base.php");
    include_once("../config.php");
    $query = '--QUERY--';
    $result = mysqli_query($conn, $query);
    echo '<table class="table table-striped">';
    --TABLE--
    echo '</tr></thead>';
    if ($result->num_rows > 0) {
        // output data of each row
        while($res = mysqli_fetch_array($result)) { 		
            echo "<tr>";
            --VARIABLES--	
        }
    }
    echo '</table>';
    $conn->close();
    $result->close();
    mysqli_close($conn);
    ?>
    </div>
    </div>
    </div>
    </body>
    </html>
    """

def indexGenerator(data):
    queryList = queryGenerator(data, 'select-all', '', '')
    count = 0
    for i in data:
        filePath = './generated_files/www/'+i+'/index.php'
        f = open(filePath,'w')
        content = base.replace('--QUERY--', queryList[count])
        count += 1
        variableStructure =''
        tableStructure = 'echo "<thead><tr>'
        for j in data[i]:
            if j != 'constraints':
                tableStructure += '<th>'+ j.upper() +'</th>'
                variableStructure += 'echo "<td>".$res['+ j +']."</td>";\n'
        content = content.replace('--VARIABLES--', variableStructure)
        content = content.replace('--TABLE--', tableStructure+'<th></th>'+'";')
        f.write(content)
        f.close()
