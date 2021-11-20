package odevbir;
import java.io.*;
import java.util.Random;
public class CreateInputFile {
    public String generateString(int k) throws IOException {
        String[][] inputFile = new String[10][500]; //Two-dimensional array to put generated numbers in it.
        GenerateString generateString = new GenerateString();//Creates GenerateString object.
        int i, j;
        String string = "";
        for (i = 0; i < 10; i++) { //Row of the input file.
            string="";
            for (j = 0; j < 500; j++) {//Column of the input file.
                inputFile[i][j] = generateString.randomNucleotide(); //Generates random nucleotides through GenerateString object.
                string = string.concat(inputFile[i][j]); //Converts two-dimensional array to string by adding each of them consecutively.
            }
            string = string + "\n"; //Switches to next row when 500 nucleotides is generated.
            string = changeInputFile(string);//Calls changeInputFile method to replace mutated k-mer.
            try{
                BufferedWriter input = new BufferedWriter(new FileWriter("input" + k + ".txt",true)); //Creates 10 input files(check Main.java)
                input.write(string);//Puts the data into the text file.
                input.close();//Closes the file.
            }
            catch(Exception e){//Error check.
                e.printStackTrace();
            }
        }
        return string;
    }
    public String mutation(StringBuilder mutation) {
        Random random = new Random();
        GenerateString generateString = new GenerateString();//Calls GenerateString object to generate 4 mutations.
        //System.out.println(mutation);
        int i;
        int newRandomNumber;
        String kmer = "";
        String nucleotide = "";
        int tempArray[] = {500,500,500,500};//Please check comment in 43th row.
        for (i = 0; i < 4; i++) {
            newRandomNumber = random.nextInt(10);//Generates random numbers between 0-9
            boolean temp = true;
            while(temp){//Basically we decide which indexes to be mutated randomly in while.
                for(int j = 0; j < 4; j++){
                    if(newRandomNumber == tempArray[j]){ //We know that newRandomNumber will never be equal to 500 since it can not be greater than 9.
                        newRandomNumber = random.nextInt(10);//Generates random numbers between 0-9
                        temp = true;
                    }
                    temp = false;
                }
                tempArray[i] = newRandomNumber;//Puts newly generated index numbers into tempArray.
            }
            nucleotide = generateString.randomNucleotide();
            while(nucleotide.charAt(0) != mutation.charAt(newRandomNumber)){//While new generated nucleotide (for mutation) is not equal to former nucleotide
                mutation.setCharAt(newRandomNumber, nucleotide.charAt(0) );//in same index, it applies the mutation.
            }
            mutation.setCharAt(newRandomNumber, nucleotide.charAt(0) );
            kmer = String.valueOf(mutation);//Converts StringBuilder to String in order to return String from this method.
        }
        return kmer;
    }
    public String changeInputFile(String str){
        StringBuilder mutationStr = new StringBuilder();
        GenerateString generateString = new GenerateString();
        int n;
        for(n = 0; n < 10 ;n++){
            mutationStr.append(generateString.randomNucleotide());//Decides which k-mer will be mutated.
        }
        String kmer = mutation(mutationStr); //Mutated kmer.
        System.out.println(kmer);
        Random random = new Random();
        int randomNumber = random.nextInt(490);//Generates random number between 0-490
        String newStr = str.replace(str.substring(randomNumber,randomNumber + 10),kmer);//Puts mutated k-mer into the text file in a random place.
        return newStr;
    }
}