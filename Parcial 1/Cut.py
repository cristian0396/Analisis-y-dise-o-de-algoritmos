#define INF 2000000000 
#define FOR (i, a, n) for (int i = a, _n = n; i <_n; i ++)

int  N, K; 
int  arr[605], pos[605];

// Comprueba si el número x que crees que satisface el número máximo de campamentos necesarios

bool check(int x){ 
     int y = x, camp = 0; 
     FOR (i, 0, N+1){ 
         int dif = pos[i+1] - pos[i]; 
         if(y >= dif) y -= dif; 
         else{ 
              camp ++; 
              y = x - dif;
         }    
         if(camp > K || y < 0) devuelve falso; 
     }      
     devuelve  verdadero ; 
}

//Principal 

int  main(){ 
    while  (scanf( "% d% d" , & N , & K) == 2){ 
          FOR  (i, 1, N+2) scanf("% d", & arr[i]);
          
          pos[0] = 0; 
          FOR  (i, 1, N+2) pos[i] = arr[i] + pos[i-1];       
          
          int izquierda = pos[0], derecha = pos[N+1]; 
          int dist = INF ;
          
          while  (  left  <=  right  ) { 
                int  mid = ((LL) left + right ) / 2 ; 
                if  ( marca(mid)) dist = min(dist , mid ), derecha = mid - 1; 
                más a la  izquierda  =  mid + 1 ; 
          }
          
          printf ( "% d \n " ,  dist ); 
    } 
    devuelve  0 ; 
}