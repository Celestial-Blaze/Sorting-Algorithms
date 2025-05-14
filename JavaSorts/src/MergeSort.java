import java.util.Arrays;

public class MergeSort {
    public static void main(String[]args){
        int[] myArray = {1,2,4,53,0,-22,42,-190,1000,29,37,3,12};
        System.out.println(Arrays.toString(myArray));
        mergeSort(myArray, 0, myArray.length - 1); // side effects :)
        System.out.println(Arrays.toString(myArray));

    }
    public static void mergeSort(int[] alist, int left, int right){
        if (left < right){
            // find midpoint to split array
            int mid = left + (right - left) / 2;
            // apparently safer because avoids integer overflow
            // kind of like in our silly half implemented Jiffy language

            // sort halves recursively
            mergeSort(alist, left, mid);
            mergeSort(alist, mid+1, right);

            // merge
            merge(alist, left, mid, right);
        }
    }
    public static void merge(int[] sublist, int left, int mid, int right) {
        // find length without using length function
        // I love how this is done knowing the constraints of the programming language implementation
        int len1 = mid - left + 1;
        int len2 = right - mid;

        // Temp arrays
        int[] L = new int[len1];
        int[] R = new int[len2];
        // I love how we kinda use functional, rather than imperative, ways to solve this

        // populate using this fancy efficient way to copy array elements
        // don't we love optimizing memory management :)
        System.arraycopy(sublist, left, L, 0, len1);
        System.arraycopy(sublist, mid +1, R, 0, len2);

        int i = 0, j = 0, k = left;
        while (i < len1 && j < len2) {
            if (L[i] <= R[j]) {
                sublist[k++] = L[i++]; // OMG I was today years old when I found out you can ++ anywhere
            } else {
                sublist[k++] = R[j++];
            }
        }
        // fill up remaining
        while (i < len1) {
            sublist[k++] = L[i++];
        }
        while (j < len2) {
            sublist[k++] = R[j++];
        }
    }
}