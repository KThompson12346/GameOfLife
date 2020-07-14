import javax.swing.JFrame;
import java.util.Random;
import java.util.Arrays;
import javax.swing.JComponent;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.Color;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.*;
import javax.swing.*;
import java.awt.BorderLayout;

public class GameOfLife extends JFrame {

  int PIXELSIZE = 10; // size of each cell
  int ROW = 75; // row of the game and will also dictate the size of the screen
  int COLUMN = 75; // column of the game and also contributes to the size of the screen
  Random random = new Random(); // will be use to randomly fill the grid with ones and zeros
  JButton start; // will be used to start the game of life

  public GameOfLife() {
    JPanel panel = new JPanel(); // used to add the start and the game of life board to the JFrame
    DrawCells cellsComp = new DrawCells(); // is the game of life cells component
    start = new JButton("Start"); // start button
    start.addActionListener(cellsComp); // adds the ActionListener to the start button
    panel.setLayout(new BorderLayout()); // gives the 'panel' the borderlayout
    start.setToolTipText("Click to start game of life");
    this.setTitle("Game Of Life: Java");
    this.setSize(PIXELSIZE * ROW, PIXELSIZE * COLUMN); // sets size of the screen using the ROW, COLUMN and PIXELSIZE
    this.setLocationRelativeTo(null); // centers the game of life screen to the center of the screen
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    panel.add(start, BorderLayout.SOUTH); // adds start button to the bottom of the panel
    panel.add(cellsComp, BorderLayout.CENTER); // adds the cells component to the panel in the center (above the start button)
    this.add(panel); // panel is added the JFrame
    this.setVisible(true);
  }

  private class DrawCells extends JComponent implements ActionListener {
    int grid[][] = new int[ROW][COLUMN]; // is the origianl grid for the game of life
    int updatedGrid[][] = new int[ROW][COLUMN]; // is the updated grid that is used to update 'grid'

    public void createGrid() { // method to create the grid and fill it with ones and zeros
      for (int i = 0; i < grid.length; i++) {
        for (int j = 0; j < grid[i].length; j++) {
          grid[i][j] = random.nextInt(2); // above two lines loops through the grid array and then at position grid[i][j] a zero or one is placed in that position
        }
      }
    }

    public void applyRules() { // method that will apply the game of life rules to the grid
      for (int i = 1; i < ROW - 1; i++) {
        for (int j = 1; j < COLUMN - 1; j++) {
          int neighboursCount = 0; // used to count the neighbours of each cell

          neighboursCount += grid[i-1][j-1]; // top left
          neighboursCount += grid[i][j-1]; // top center
          neighboursCount += grid[i+1][j-1]; // top right

          neighboursCount += grid[i-1][j]; // middle left
          neighboursCount += grid[i+1][j]; // middle right

          neighboursCount += grid[i-1][j+1]; // top left
          neighboursCount += grid[i][j+1]; // top center
          neighboursCount += grid[i+1][j+1]; // top right

          // Game of Life rules:

          // Alive cells:
          if (grid[i][j] == 1) {
            // rule 1 any live cell with fewer than two live neighboours dies, as if by underpopulation
            if (neighboursCount < 2) {
              updatedGrid[i][j] = 0;
            }
            // rule 2 any live cell with two or three live neighbours, lives on to the generation
            else if (neighboursCount == 2 || neighboursCount == 3) {
              updatedGrid[i][j] = 1;
            }
            // rule 3 any live cell with more than three live neighbours dies, as if by overpopulation
            else if (neighboursCount > 3 && neighboursCount <= 8) {
              updatedGrid[i][j] = 0;
            }
            else {
              updatedGrid[i][j] = 0;
            }
          }
          // Dead cells
          else if (grid[i][j] == 0) {
            // rule 4 any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
            if (neighboursCount == 3) {
              updatedGrid[i][j] = 1;
            }
            else {
              updatedGrid[i][j] = 0;
            }
          }
        }
      }
      for (int i = 0; i < ROW; i++) {
        for (int j = 0; j < COLUMN; j++) {
          grid[i][j] = updatedGrid[i][j]; // the original grid is now updated with the updated grid
        }
      }
    }

    public void paintComponent(Graphics g) { // method to display the cells on the screen
      super.paintComponent(g);
      Graphics2D g2 = (Graphics2D) g;
      for (int i = 0; i < ROW; i++) {
        for (int j = 0; j < COLUMN; j++) {
          if (grid[i][j] == 1) { // if a one is in position grid[i][j] then a rectangle is drawn on the screen
            g2.setColor(Color.RED);
            g2.fillRect(i * PIXELSIZE, j * PIXELSIZE, PIXELSIZE, PIXELSIZE); // a rectangle is drawn in the position specified i*PIXELSIZE and j*PIXELSIZE  with the width and height of PIXELSIZE
          }
        }
      }
    }

  Timer animation;
  public void actionPerformed(ActionEvent e) { // actionPerformed() method to give instructions to the start button
    if (e.getSource() == start && animation == null) { // if the start button is clicked and the animation has not started then following is executed
        createGrid(); // createGrid() method is called to initialize the grid
        int delay = 100; // this is the time delay used with the timer
        ActionListener taskPerformer = new ActionListener() { // another ActionListener is created to be used with the Timer object 'animation'
            public void actionPerformed(ActionEvent evt) { // this actionPerformed() is used with taskPerformer to apply the game of life rules and repaint the cells on the screen
                applyRules();
                repaint();
            }
        };
        animation = new Timer(delay, taskPerformer); // a new Timer object is created with the delay and the taskPerformer ActionListener i.e. Timer will keep applying the game of life rules and repaint the cells
        animation.start(); // the timer object is started
      }
    }
  }

  public static void main(String[] args) {
    GameOfLife gol = new GameOfLife(); 
  }
}
