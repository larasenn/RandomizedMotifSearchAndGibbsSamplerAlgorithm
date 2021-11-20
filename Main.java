package odevbir;
import java.io.IOException;
public class Main {
    public static void main(String[] args) throws IOException {
        CreateInputFile createInputFile = new CreateInputFile();//Creates CreateInputFile object.
        int k;
        for(k = 0; k < 10 ; k++){
            createInputFile.generateString(k);//Creates 10 input files randomly.
        }
    }
}
