import java.util.Arrays;

public class QuickSort {
    public static void main(String[]args){
        System.out.println("QuickSort");
        int[] myArray = {1,2,4,53,0,-22,42,-190,0,29,1000,29,37,3,12};
        System.out.println(Arrays.toString(myArray));
        quickSort(myArray, 0, myArray.length - 1); // side effects :)
        System.out.println(Arrays.toString(myArray));

    }
    public static void quickSort(int[] alist, int low, int high){
        if (low < high) {
            // get pivot using our fav partitioning algorithm
            int p = hoarePartition(alist, low, high);

            // recursively sort elements around partition
            quickSort(alist, low, p);
            quickSort(alist, p + 1, high);
        }
    }

    private static int hoarePartition(int[] theList, int low, int high) {
        int pivot = theList[low]; // first element
        int i = low - 1;
        int j = high + 1;

        while (true) {
            // move i indices right until we cross the pivot value
            do {
                i++;
            } while (theList[i] < pivot);

            // move j indices left until we cross the pivot value
            do {
                j--;
            } while (theList[j] > pivot);

            // pointers crossing
            if (i >= j) return j;

            // swap ith & jth elements
            swap(theList, i, j);
        }
    }

    private static void swap(int[] alist, int i, int j) {
        // swap be doing swap things
        int temp = alist[i];
        alist[i] = alist[j];
        alist[j] = temp;
    }
}
