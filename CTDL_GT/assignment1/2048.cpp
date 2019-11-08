//CTDL&GT
//Assignment 1
//Ho va ten: Nguyen Duc Huy
//MSHV: 1870567

#include <iostream>
#include <cstdlib>

using namespace std;

const int max_value = 2048;
static int score;
int matrix [4][4]={0};

// Create random position to add new element: 0,1,2,3 (25%)
int random_position_generate(){
    int random_index = rand() % 4;
    return random_index;
}

//Create random value: 2(80%) or 4(20%) 
int random_value_generate(){
    int random_element = rand() % 10;
    random_element = (random_element>=8) ? 4 : 2;
    return random_element;
}

//check if max value = 2048
int win(){
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            if(matrix[i][j]==max_value){
                return 1;
            }
        }
    }
    return 0;
}

//check if there is no blank index and no merge case
int game_over(){
    int game_over = 1;
    for(int i=0; i<4; i++){
        for(int j=0; j<3; j++){
            if(matrix[i][j]==0 || matrix[i][j+1]==0 || matrix[i][j] == matrix[i][j+1]){
                game_over = 0;
                break;
            }
        }
    }
    for(int j=0; j<4; j++){
        for(int i=0; i<3; i++){
            if(matrix[i][j]==0 || matrix[i+1][j]==0 || matrix[i][j] == matrix[i+1][j]){
                game_over = 0;
                break;
            }
        }
    }
    return game_over;
}

//Init value and display for new game
void first_display(){
    int index_i1, index_j1, index_i2, index_j2;
    while(1){
        index_i1 = random_position_generate();
        index_j1 = random_position_generate();
        index_i2 = random_position_generate();
        index_j2 = random_position_generate();
        if(index_i1==index_i2 && index_j1==index_j2){
            continue;
        }
        else
            break;
    }
    cout<<"------2048------"<<endl;
    cout<<"----New game----"<<endl;
    cout<<"Rules:"<<endl;
    cout<<"Use w(up), s(down), a(left), d(right) and q(quit)"<<endl;
    for(int i=0; i<4; i++){
        cout<<"|-----------------------|"<<endl;
        for(int j=0; j<4; j++){
            cout<<"|";
            if(i==index_i1 && j==index_j1){
                matrix[i][j]=2;
                cout<<"  "<<2<<"  ";
            }
            else if(i==index_i2 && j==index_j2){
                int temp = random_value_generate();
                matrix[i][j] = temp;
                cout<<"  "<<temp<<"  ";
            }
                else
                    cout<<"     ";
        }
        cout<<"|"<<endl;
    }
    cout<<"|-----------------------|"<<endl;
    
}

//Display the matrix value
void display(){
    for(int i=0; i<4; i++){
            cout<<"|-----------------------|"<<endl;
            for(int j=0; j<4; j++){
                cout<<"|";
                if(matrix[i][j]!=0){
                    if(matrix[i][j]==1024 || matrix[i][j]==2048)
                        cout<<" "<<matrix[i][j];
                    if(matrix[i][j]==128 || matrix[i][j]==256 || matrix[i][j]==512)
                        cout<<" "<<matrix[i][j]<<" ";
                    if(matrix[i][j]==16 || matrix[i][j]==32 || matrix[i][j]==64)
                        cout<<"  "<<matrix[i][j]<<" ";
                    if(matrix[i][j]==2 || matrix[i][j]==4 || matrix[i][j]==8)
                        cout<<"  "<<matrix[i][j]<<"  ";
                }
                else
                    cout<<"     ";
            }
            cout<<"|"<<endl;
        }
        cout<<"|-----------------------|"<<endl;
}

//insert random element
void add_element(){
    int index_i, index_j;
    int flag=0;
    while(1){
        if(flag==1)break;
        index_i = random_position_generate();
        index_j = random_position_generate();
        if(matrix[index_i][index_j]==0){
            matrix[index_i][index_j] = random_value_generate();
            flag=1;
        }
    }
}

//move
void left(){
    int flag=0;
    for(int i=0; i<4; i++){
        int n=0;
        int prev=0;
        for (int j=0; j<4; j++)
        {
            if (n==matrix[i][j] && n!=0){
                matrix[i][prev] = 2*n;
                matrix[i][j] = 0;
                score+=2*n;
                n = 0;
                flag++;
                continue;
            }
            if (matrix[i][j]!=0){
                n = matrix[i][j];
                prev = j;
            }
        }
    }
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            for(int k=0; k<3; k++){
                if(matrix[i][k]==0 && matrix[i][k+1]!=0){
                    matrix[i][k]=matrix[i][k]^matrix[i][k+1];
                    matrix[i][k+1]=matrix[i][k]^matrix[i][k+1];
                    matrix[i][k]=matrix[i][k]^matrix[i][k+1];
                    flag++;
                }
            }
        }
    }
    if(flag!=0){
        add_element();
    }
    display();
}

void right(){
    int flag=0;
    for(int i=0; i<4; i++){
        int n=0;
        int prev=0;
        for (int j=3; j>=0; j--)
        {
            if (n==matrix[i][j] && n!=0){
                matrix[i][prev] = 2*n;
                matrix[i][j] = 0;
                score+=2*n;
                n = 0;
                flag++;
                continue;
            }
            if (matrix[i][j]!=0){
                n = matrix[i][j];
                prev = j;
            }
        }
    }
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            for(int k=3; k>0; k--){
                if(matrix[i][k]==0 && matrix[i][k-1]!=0){
                    matrix[i][k]=matrix[i][k]^matrix[i][k-1];
                    matrix[i][k-1]=matrix[i][k]^matrix[i][k-1];
                    matrix[i][k]=matrix[i][k]^matrix[i][k-1];
                    flag++;
                }
            }
        }
    }
    if(flag!=0){
        add_element();
    }
    display();
}

void up(){
    int flag=0;
    for(int i=0; i<4; i++){
        int n=0;
        int prev=0;
        for (int j=0; j<4; j++)
        {
            if (n==matrix[j][i] && n!=0){
                matrix[prev][i] = 2*n;
                matrix[j][i] = 0;
                score+=2*n;
                n = 0;
                flag++;
                continue;
            }
            if (matrix[j][i]!=0){
                n = matrix[j][i];
                prev = j;
            }
        }
    }
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            for(int k=0; k<3; k++){
                if(matrix[k][i]==0 && matrix[k+1][i]!=0){
                    matrix[k][i]=matrix[k][i]^matrix[k+1][i];
                    matrix[k+1][i]=matrix[k][i]^matrix[k+1][i];
                    matrix[k][i]=matrix[k][i]^matrix[k+1][i];
                    flag++;
                }
            }
        }
    }
    if(flag!=0){
        add_element();
    }
    display();
}

void down(){
    int flag=0;
    for(int i=0; i<4; i++){
        int n=0;
        int prev=0;
        for (int j=3; j>=0; j--)
        {
            if (n==matrix[j][i] && n!=0){
                matrix[prev][i] = 2*n;
                matrix[j][i] = 0;
                score+=2*n;
                n = 0;
                flag++;
                continue;
            }
            if (matrix[j][i]!=0){
                n = matrix[j][i];
                prev = j;
            }
        }
    }
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            for(int k=3; k>0; k--){
                if(matrix[k][i]==0 && matrix[k-1][i]!=0){
                    matrix[k][i]=matrix[k][i]^matrix[k-1][i];
                    matrix[k-1][i]=matrix[k][i]^matrix[k-1][i];
                    matrix[k][i]=matrix[k][i]^matrix[k-1][i];
                    flag++;
                }
            }
        }
    }
    if(flag!=0){
        add_element();
    }
    display();
}

int main(){
    char ch;
    int end = 0;

    //initialize matrix
    first_display();

    while(1){
        if(win()){
            cout<<"YOU WIN!!!"<<endl;
            end = 1;
        }
        if(game_over()){
            cout<<"GAME OVER!!!"<<endl;
            end = 1;
        }

        if (end==1){
            cout<<"Do you want to make a new game? (y/n)"<<endl;
            cin>>ch;
            if (ch=='y'){
                //reset the matrix
                for(int i=0; i<4; i++){
                    for(int j=0; j<4; j++){
                        matrix[i][j] = 0;
                    }
                }
                first_display();
                end = 0;
            }
            if (ch=='n'){
                exit(1);
            }
        }
        else {
            cin>>ch;
            switch (ch) {
                case 'w':
                    up();
                    break;
                case 's':
                    down();
                    break;
                case 'a':
                    left();
                    break;
                case 'd':
                    right();
                    break;
                case 'q':
                    exit(1);
                default:
                    break;
            }
            //show current scores
            cout<<"score: "<<score<<endl;
        }        
    }
    return 0;
}

