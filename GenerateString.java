package odevbir;
import java.util.Random;
public class GenerateString {
    public String randomNucleotide(){ //This method basically generates a nucleotide according to randomly generated number.
        Random random = new Random(); //in order to create DNA sequences and put them into input file.
        int randomNumber = random.nextInt(4);//Generates random number between 0-3.
        if(randomNumber == 0){ //If generated number  is 0, then return "G" nucleotide.
            return "G";
        }else if(randomNumber == 1){ //If generated number  is 1, then return "C" nucleotide.
            return "C";
        }
        else if(randomNumber == 2){ //If generated number  is 2, then return "A" nucleotide.
            return "A";
        }
        else if(randomNumber == 3){ //If generated number  is 3, then return "T" nucleotide.
            return "T";
        }
        else{ //Error check.
            throw new java.lang.Error("Error has occured.");
        }
    }
}
