#include <iostream>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <iomanip>
#include <cstring>
#include <cmath>

using namespace std;

class Boardgame {
    private:
        int **board;
        int dimension;
        bool playerWon = false; ///Attribute to store if the player achieved 2048
        bool playerContinue = false; ///Attribute to store if the player would like to continue
                                     ///playing after they have achieved 2048

        bool checkValidMovement(char input){
            switch(input){
                case 'w':
                    for(int j=0;j<dimension;j++){
                        for(int i=0;i<dimension;i++){
                            if(i == 0){ /// Just so we don't have any problems of accessing invalid memory locations
                                if(board[i][j] == 0)
                                    return true;
                            }
                            else {
                                ///If it is 0 or there is a possible combination of adjacent cells
                                if(board[i][j] == 0 || board[i][j] == board[i-1][j])
                                    return true;
                            }
                        }
                    }
                    ///If it got to this point, then it is not a valid movement
                    return false;
                case 'a':
                    for(int i=0;i<dimension;i++){
                        for(int j=0;j<dimension;j++){
                            if(j == 0){ /// Just so we don't have any problems of accessing invalid memory locations
                                if(board[i][j] == 0)
                                    return true;
                            }
                            else {
                                ///If it is 0 or there is a possible combination of adjacent cells
                                if(board[i][j] == 0 || board[i][j] == board[i][j-1])
                                    return true;
                            }
                        }
                    }
                    ///If it got to this point, then it is not a valid movement
                    return false;
                case 's':
                    for(int j=0;j<dimension;j++){
                        for(int i=dimension-1;i>-1;i--){
                            if(i == dimension - 1){ /// Just so we don't have any problems of accessing invalid memory locations
                                if(board[i][j] == 0)
                                    return true;
                            }
                            else {
                                ///If it is 0 or there is a possible combination of adjacent cells
                                if(board[i][j] == 0 || board[i][j] == board[i+1][j])
                                    return true;
                            }
                        }
                    }
                    ///If it got to this point, then it is not a valid movement
                    return false;
                case 'd':
                    for(int i=0;i<dimension;i++){
                        for(int j=dimension-1;j>-1;j--){
                            if(j == dimension - 1){ /// Just so we don't have any problems of accessing invalid memory locations
                                if(board[i][j] == 0)
                                    return true;
                            }
                            else {
                                ///If it is 0 or there is a possible combination of adjacent cells
                                if(board[i][j] == 0 || board[i][j] == board[i][j+1])
                                    return true;
                            }
                        }
                    }
                    ///If it got to this point, then it is not a valid movement
                    return false;
                default:
                    ///It probably will never get to this point
                    return false;
            }
        }

        void getPlayerInput(){
            char input;
            int nCombination; ///To help maintain the maxCombination threshold
            int maxCombination = dimension/2;
            ///maxCombination is really important here. It avoids the game to combine "excessively" in a row/column
            ///For example, suppose we have the following state and suppose the player hit the 'w' key(move up):
            ///  Current state:      Without maxCombination:            Original game after 'w' move:
            ///  2     0     0       8     0     0                      4     0     0
            ///  2     0     0       0     0     0                      4     0     0
            ///  4     0     0       0     0     2(random new value)    0     0     2(random new value)
            while(true){
                cout << "Please type 'w', 'a', 's' or 'd' regarding to your desired movement: ";
                cin >> input;
                if(!checkValidMovement(input)){
                    cout << "That movement is not available given the current game, please input another movement." << endl;
                    continue;
                }
                if(lostGame()){ ///If there is not at least one movement available
                    cout << "You lost the game!" << endl;
                    break;
                }
                switch(input){
                    case 'w':
                        for(int j=0;j<dimension;j++){
                            nCombination = 0; ///It is set to 0 for every new column
                            for(int i=0;i<dimension;i++){
                                while(true){
                                    if(i == 0) /// If the cell is is at the top
                                        break;      /// then get out of the internal loop
                                    ///If they have the same value, combine them
                                    if(board[i][j] == board[i-1][j] && board[i][j] !=0 && nCombination <= maxCombination){
                                        board[i-1][j] = board[i-1][j] + board[i][j];
                                        board[i][j] = 0;
                                        nCombination++;
                                    }
                                    else { /// So, they do not combine
                                        if (board[i][j] !=0 && board[i-1][j] == 0){ ///If the cell above is empty
                                            board[i-1][j] = board[i][j];
                                            board[i][j] = 0;
                                            i--;
                                        }
                                        else /// So there's nothing left to do, skip to the next cell
                                            break;
                                    }

                                }
                            }
                        }
                        break;

                    case 'a':
                        for(int i=0;i<dimension;i++){
                            nCombination = 0; ///It is set to 0 for every new row
                            for(int j=0;j<dimension;j++){
                                while(true){
                                    if(j == 0) /// If the cell is is at the far left
                                        break;      /// then get out of the internal loop
                                    ///If they have the same value, combine them
                                    if(board[i][j] == board[i][j-1] && board[i][j] !=0 && nCombination <= maxCombination){
                                        board[i][j-1] = board[i][j-1] + board[i][j];
                                        board[i][j] = 0;
                                        nCombination++;
                                    }
                                    else { /// So, they do not combine
                                        if (board[i][j] !=0 && board[i][j-1] == 0){ ///If the cell on the left is empty
                                            board[i][j-1] = board[i][j];
                                            board[i][j] = 0;
                                            j--;
                                        }
                                        else /// So there's nothing left to do, skip to the next cell
                                            break;
                                    }

                                }
                            }
                        }
                        break;

                    case 's':
                        for(int j=0;j<dimension;j++){
                            nCombination = 0; ///It is set to 0 for every new row
                            for(int i=dimension-1;i>-1;i--){
                                while(true){
                                    if(i == dimension-1) /// If the cell is is at the bottom
                                        break;      /// then get out of the internal loop
                                    ///If they have the same value, combine them
                                    if(board[i][j] == board[i+1][j] && board[i][j] !=0 && nCombination <= maxCombination){
                                        board[i+1][j] = board[i+1][j] + board[i][j];
                                        board[i][j] = 0;
                                        nCombination++;
                                    }
                                    else { /// So, they do not combine
                                        if (board[i][j] !=0 && board[i+1][j] == 0){ ///If the cell below is empty
                                            board[i+1][j] = board[i][j];
                                            board[i][j] = 0;
                                            i++;
                                        }
                                        else /// So there's nothing left to do, skip to the next cell
                                            break;
                                    }

                                }
                            }
                        }
                        break;

                    case 'd':
                        for(int i=0;i<dimension;i++){
                            nCombination = 0; ///It is set to 0 for every new row
                            for(int j=dimension-1;j>-1;j--){
                                while(true){
                                    if(j == dimension-1) /// If the cell is is at the far right
                                        break;      /// then get out of the internal loop
                                    ///If they have the same value, combine them
                                    if(board[i][j] == board[i][j+1] && board[i][j] !=0 && nCombination <= maxCombination){
                                        board[i][j+1] = board[i][j+1] + board[i][j];
                                        board[i][j] = 0;
                                        nCombination++;
                                    }
                                    else { /// So, they do not combine
                                        if (board[i][j] !=0 && board[i][j+1] == 0){ ///If the cell on the right is empty
                                            board[i][j+1] = board[i][j];
                                            board[i][j] = 0;
                                            j++;
                                        }
                                        else /// So there's nothing left to do, skip to the next cell
                                            break;
                                    }

                                }
                            }
                        }
                        break;

                    default:
                        cout << "Please type in a valid movement!" << endl;
                        break;
                }
                break; ///In order to get out of the while(true)
            }
        }

        bool lostGame(){
            if(checkValidMovement('w') && checkValidMovement('a') &&
               checkValidMovement('s') && checkValidMovement('d'))
                return false;
            else
                return true;
        }

        ///Chances are 80% and 20% to appear a number 2 and 4, respectively.
        ///Regarding to the choice of the cell, chances are 100% random
        ///based on the remaining free cells.
        void randomiseNewValue(){
            int value = generateRandomNumber(10);
            ///Go through the board to check the positions available
            ///and store them in a vector
            vector<int> available;
            for(int i=0;i<dimension;i++)
                for(int j=0;j<dimension;j++)
                    if(board[i][j] == 0)
                        available.push_back(dimension * i + j);
            int position = available[generateRandomNumber(available.size())];

            if(value <= 7) /// Value of 2
                board[position/dimension][position%dimension] = 2;
            else /// Value of 4
                board[position/dimension][position%dimension] = 4;
        }

        void printBoard(){
            int highestNumber = 0;
            char continuePlaying;
            int nCharacter;
            for(int i=0;i<dimension;i++)
                for(int j=0;j<dimension;j++)
                    if(board[i][j] > highestNumber)
                        highestNumber = board[i][j];
            if(highestNumber == 2048 && playerWon == false && playerContinue == false){
                cout << "You won the game! Congratulations!!!" << endl << endl;
                cout << "Would you like to continue playing? [y/n]: ";
                cin >> continuePlaying;
                playerWon = true;
                if(continuePlaying == 'y')
                    playerContinue = true;
                else
                    exit(1);
            }
            nCharacter = highestNumber > 0 ? (int) log10 ((double) highestNumber) + 1 : 1;
            for(int i=0;i<dimension;i++){
                for(int j=0;j<dimension;j++)
                    cout << setw(nCharacter) << board[i][j] << " ";
                cout << endl;
            }
            cout << endl;
        }

        int generateRandomNumber(int limit){
            return rand() % limit;
        }

    public:
        Boardgame(int dimension){
            ///Initialisation of the attributes
            this->dimension = dimension;
            board = new int*[dimension];
            for(int i=0;i<dimension;i++)
                board[i] = new int[dimension];
        }

        void startGame(){
        ///First we fill in the board with 0's(meaning it is empty)
            for(int i=0;i<dimension;i++)
                for(int j=0;j<dimension;j++)
                    board[i][j] = 0;
            ///Then now we need to randomise in which cell is going
            ///to start with a value, and which value is this (2 or 4)
            srand(time(0));
            int initialValue = generateRandomNumber(10); /// 0-7 for 2 and 8-9 for 4
            int initialPosition = generateRandomNumber(dimension*dimension);
            ///The board will be sketched like this:
            ///For dimension 3:         For dimension 4:
            /// 0 1 2                   0  1  2  3
            /// 3 4 5                   4  5  6  7            And so on... 13 = [3][1]
            /// 6 7 8                   8  9  10 11
            ///                         12 13 14 15
            if(initialValue <= 7) /// Value of 2
                board[initialPosition/dimension][initialPosition%dimension] = 2;
            else /// Value of 4
                board[initialPosition/dimension][initialPosition%dimension] = 4;

            ///Print the initial state of the game
            printBoard();

            ///Now we are ready for the main loop of the game

            while(true){
                getPlayerInput();
                if(lostGame()){ ///If there is not at least one movement available
                    cout << "You lost the game!" << endl;
                    break;
                }
                randomiseNewValue();
                printBoard();
            }
        }
};
int main(){
    srand(time(0));
    int dimension;
    cout << "Please type in the wanted game dimension: ";
    cin >> dimension;
    Boardgame board(dimension);
    board.startGame();
    return 0;
}
