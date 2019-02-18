$(function(event) {

    var GRIDWIDTH = 100;
    var GRIDHEIGHT = 100;
    var gameGrid[] = createGrid(GRIDHEIGHT); //

    //creates the grid for the game, using an array of empty arrays
    function createGrid(rows) {
      var gridArray[]; //is the game grid
      //for loop that creates the grid array, each element is an empty array to create the multi-dimensional array
      for (var i = 0; i < ROWS; i++) {
        gridArray[i] = [];
      }
    return gridArray;
    }

    //will populate the grid randomly with alive and dead cells
    function populateGrid() {
      for (var rows = 0; rows < GRIDHEIGHT; rows++) { //goes across the rows within the grid
        for (var cols = 0; cols < GRIDWIDTH; cols++) { //goes across the columns within the grid
            var cell = Math.floor(Math.Random() * 2 ) //the cells of the grid is either a 1 or 0 (alive or dead), chosen at random
            if (cell === 1) { //if the cell variable is the same as the integer value 1 and same type int then the element at gameGrid[rows][cols] is set to a 1 else a 0, this is done randomly.
            gameGrid[rows][cols] = 1;
          }
          else {
            gameGrid[rows][cols] = 0;
          }
        }
      }
    }

    //Will draw the game grid on the screen including cells
    function drawGrid() {
      var gameCanvas = $("#gameCanvas"); //gets the gameCanvas element
      var ctx = $("#gameCanvas")[0].getContext("2d");
      ctx.clearRect(0, 0, 100, 100);
      //both loops go through the rows and columns respectively and draws the pixel in the grid in the specified colour
      for (var rows = 1; rows < GRIDHEIGHT; rows++) {
        for (var cols = 1; cols < GRIDWIDTH; cols++) {
          if (gameGrid[rows][cols] === 1) { //if the element is a 1 the pixel is coloured to represent it is alive
            context.fillStyle = “#FF0000”;
            context.fillRect(rows, cols, 1, 1);
          }
        }
      }
    }

    

})
