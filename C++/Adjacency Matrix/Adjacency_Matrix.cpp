#include <stdio.h>
#include <stdlib.h>

#define N 8
int main() {
	char graf[N] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'};
	int x[N][N] = {
		0,1,1,0,0,0,0,0,
		0,0,0,1,1,0,0,0,
		0,0,0,0,0,1,1,0,
		0,0,0,0,0,0,0,1,
		0,0,0,0,0,0,0,1,
		0,0,0,0,0,0,0,1,
		0,0,0,0,0,0,0,1,
		0,0,0,0,0,0,0,1
	};
	int i, s;
	
	//Output Graf
	printf("Graf Terdiri Dari Simpul : ");
	
	for(i = 0; i < N; i++) {
		printf("%c", graf[i]);
	}
	printf("\n");
	
	//Output Simpul Yang Terhubung
	for(i = 0; i < N; i++) {
		printf("\nSimpul %c Terhubung Dengan : ", graf[i]);
		for(s = 0; s < 8; s++) {
			if(x[i][s]==1)
				printf("%c", graf[s]);
			else
				printf(NULL);
		}
	}
}