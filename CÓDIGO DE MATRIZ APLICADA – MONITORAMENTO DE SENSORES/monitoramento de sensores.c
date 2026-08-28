#include <stdio.h>

int main() {
    float sensores[5][24];
    float soma_sensor, soma_geral = 0;
    float maior_temp;
    int sensor_maior = 1, hora_maior = 0;
    float limite;
    int acima_limite = 0;

    // Entrada de dados
    printf("--- Leitura das Medicoes ---\n");

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 24; j++) {
            printf("Sensor %d, Hora %dh: ", i + 1, j);
            scanf("%f", &sensores[i][j]);
        }
    }

    // Inicializa a maior temperatura com o primeiro elemento
    maior_temp = sensores[0][0];

    // Processamento dos dados
    printf("\n--- Resultados ---\n");

    for (int i = 0; i < 5; i++) {
        soma_sensor = 0.0;

        for (int j = 0; j < 24; j++) {

            // Soma das temperaturas
            soma_sensor += sensores[i][j];
            soma_geral += sensores[i][j];

            // Verifica a maior temperatura
            if (sensores[i][j] > maior_temp) {
                maior_temp = sensores[i][j];
                sensor_maior = i + 1;
                hora_maior = j;
            }
        }

        printf("Media do Sensor %d: %.2f °C\n",
               i + 1, soma_sensor / 24);
    }

    // Media geral das 120 medições
    printf("Media Geral do Sistema: %.2f °C\n",
           soma_geral / 120);

    // Maior temperatura e localização
    printf("Maior Temperatura: %.2f °C (Sensor %d, as %dh)\n",
           maior_temp, sensor_maior, hora_maior);

    // Limite de temperatura
    printf("\nDigite o limite de temperatura para verificacao: ");
    scanf("%f", &limite);

    // Conta temperaturas acima do limite
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 24; j++) {
            if (sensores[i][j] > limite) {
                acima_limite++;
            }
        }
    }

    printf("Quantidade de leituras acima de %.2f °C: %d\n",
           limite, acima_limite);

    return 0;
}
