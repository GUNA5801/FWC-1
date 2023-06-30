#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    // Initialize I/O Ports
    DDRB |= (1 << PB0);  // Set PB0 as output
    DDRB &= ~(1 << PB1); // Set PB1 as input
    PORTB |= (1 << PB1); // Enable pull-up on PB1

    // Define states
    enum state { S0, S1, S2, S3, S4 } current_state = S0;

    while (1)
    {
        // Read input
        int input = PINB & (1 << PB1);

        // State transitions
        switch (current_state)
        {
            case S0:
                if (input == 0) {
                    current_state = S1;
                }
                break;
            case S1:
                if (input == 1) {
                    current_state = S2;
                }
                break;
            case S2:
                if (input == 0) {
                    current_state = S3;
                }
                break;
            case S3:
                if (input == 1) {
                    current_state = S4;
                }
                break;
            case S4:
                if (input == 0) {
                    PORTB |= (1 << PB0); // Output 1
                    _delay_ms(500);     // Wait 500ms
                    PORTB &= ~(1 << PB0);// Output 0
                    current_state = S0;
                }
                break;
            default:
                current_state = S0;
                break;
        }
    }

    return 0;
}
