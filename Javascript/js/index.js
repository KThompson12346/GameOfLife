$(function(event) {

    var GRIDWIDTH = 400;
    var GRIDHEIGHT = 400;
    var gameGrid = createGrid(GRIDWIDTH); //Grid used to display the grid
    var newGameGrid = createGrid(GRIDWIDTH); //Grid used to update game state

    //creates the grid for the game, using an array of empty arrays
    function createGrid(rows) {
      var gridArray = []; //is the game grid
      //for loop that creates the grid array, each element is an empty array to create the multi-dimensional array
      for (var i = 0; i < rows; i++) {
        gridArray[i] = [];
      }
    return gridArray;
    }

    //will populate the grid randomly with alive and dead cells
    function populateGrid() {
      for (var rows = 0; rows < GRIDHEIGHT; rows++) { //goes across the rows within the grid
        for (var cols = 0; cols < GRIDWIDTH; cols++) { //goes across the columns within the grid
            var cell = Math.floor(Math.random() * 2 ); //the cells of the grid is either a 1 or 0 (alive or dead), chosen at random
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
      var ctx = $("#gameCanvas")[0].getContext("2d"); //Gets the gameCanvas element and returns the context of the element 2d
      ctx.clearRect(0, 0, 400, 400);
      //both loops go through the rows and columns respectively and draws the pixel in the grid in the specified colour
      for (var rows = 1; rows < GRIDHEIGHT; rows++) {
        for (var cols = 1; cols < GRIDWIDTH; cols++) {
          if (gameGrid[rows][cols] === 1) { //if the element is a 1 the pixel is coloured (red) to represent it is alive
            ctx.fillStyle = "#FF0000";
            ctx.fillRect(rows, cols, 1, 1); //Size of the pixels
          }
        }
      }
    }

    // //this function will update the grid to show the new position of the pixels
    function updateGrid() {
      for (var rows = 1; rows < GRIDHEIGHT - 1; rows++) {
        for (var cols = 1; cols < GRIDWIDTH - 1; cols++) {
          var totalNeighbours = 0; //holds the total neighbours a cell has
          //calculations to add the neighbours
          totalNeighbours += gameGrid[rows-1][cols-1]; //top left
          totalNeighbours += gameGrid[rows-1][cols]; //top center
          totalNeighbours += gameGrid[rows-1][cols+1] //top right

          totalNeighbours += gameGrid[rows][cols-1] //middle left
          totalNeighbours += gameGrid[rows][cols+1] //middle right

          totalNeighbours += gameGrid[rows+1][cols-1] //bottom left
          totalNeighbours += gameGrid[rows+1][cols] //bottom center
          totalNeighbours += gameGrid[rows+1][cols+1] //bottom right

          //Game of life rules:

          //alive cell rules
          if (gameGrid[rows][cols] === 1) {
              //rule 1 any live cell with fewer than two live neighbours dies, as if by underpopulation
              if (totalNeighbours < 2) {
                newGameGrid[rows][cols] = 0;
              }
              //rule 2 any live cell with two or three live neighbours lives on to the next generation
              else if (totalNeighbours == 2 || totalNeighbours == 3) {
                newGameGrid[rows][cols] = 1;
              }
              //rule 3 any live cell with more than three live neighbours dies, as if by overpopulation
              else if (totalNeighbours > 3 && totalNeighbours <= 8) {
                newGameGrid[rows][cols] = 0;
              }
              else {
                newGameGrid[rows][cols] = 0;
              }
          }
          //dead cell rule 4 any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
          else if (gameGrid[rows][cols] === 0) {
            if (totalNeighbours == 3) {
              newGameGrid[rows][cols] = 1;
            } else {
                newGameGrid[rows][cols] = 0;
              }
            }
          }
        }
        //iterate through the rows and columns and gameGrid is set to the newGameGrid with the updated cells in the grid
        for (var rows = 0; rows < GRIDWIDTH; rows++) {
          for (var cols = 0; cols < GRIDHEIGHT; cols++) {
            gameGrid[rows][cols] = newGameGrid[rows][cols];
          }
        }
      }

      populateGrid();
      start();

      function start() {
        drawGrid();
        updateGrid();
        requestAnimationFrame(start);
      }
    })
