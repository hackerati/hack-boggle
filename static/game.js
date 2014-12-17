//
// Game logic
//
// Use proper event handling for triggering these function calls

function isValidWord() {
    // using client gameboard state, 
    // get response from server, render to client as alert or modal
    // use extra functions and callbacks as needed

    return true;
}

function newGameBoard() {
    // clear old board client-side
    // get new board server-side
    // render new board client-side

    $.ajax({
        type: "GET",
        url: "/game/new_board/",
        dataType: 'json',
        success: function(data) {

            // clear old table
            $('div.starter-template table tbody').empty();

            // render new table
            var t = $('div.starter-template table tbody');
            for (var i=0; i<data.length; i++) {
                t.append('<tr>');
                for (var j=0; j<data[i].length; j++) {
                    t.append('<td>'+data[i][j]+'</td>');
                }
                t.append('</tr>');
            }
        }
    });

    return;
}

$('div.starter-template table tbody td').on('click', userClick);

function userClick() {
    // determine if what the user clicked was valid
    //
    // valid move is up, down, left, or right of 
    // where the current selected tile is
    //
    // if no tile clicked, user may click anywhere
    //
    
    console.log(this);

    return;
}
