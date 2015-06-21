import java.io.*;
import java.util.*;

public class IsOpenNow {
    private static final HashMap<String,Integer> youbimap = new HashMap<>();
    static {
        youbimap.put("Mon",0);
        youbimap.put("Tue",1);
        youbimap.put("Wed",2);
        youbimap.put("Thu",3);
        youbimap.put("Fri",4);
        youbimap.put("Sat",5);
        youbimap.put("Sun",6);
    }

    private final String[] days;
    private final int[] opentime;
    private final int[] closetime;
    private final int filesize;

    public IsOpenNow(String filename) throws IOException {
        File file=new File(filename);
        BufferedReader br=new BufferedReader(new FileReader(file));
        filesize =Integer.parseInt(br.readLine());

        days = new String[filesize];  //曜日
        opentime = new int[filesize];  //開店
        closetime = new int[filesize]; //閉店

        for(int t = 0;t < filesize; t++) {  //初期化
            days[t] = "";
            opentime[t] = 0;
            closetime[t] = 0;
        }

        String str = br.readLine();
        for (int i = 0; str != null; i++){
            String[] opendata = str.split(",");  //区切る
            days[i] = opendata[0];
            opentime[i] = Integer.parseInt(opendata[1]);  //commaの前
            closetime[i] = Integer.parseInt(opendata[2]);  //commaの後
            str = br.readLine();
        }
        br.close();
    }

    public boolean isOpenNow(String Day, int hour, int minute) {
        if (!youbimap.containsKey(Day)) {
            throw new IllegalArgumentException("Invalid Day.");
        }
        if (hour < 0 || hour > 24) {
            throw new IllegalArgumentException("Invalid hour.");
        }
        if (minute < 0 || minute > 60 || (hour == 24 && minute != 0)) {
            throw new IllegalArgumentException("Invalid minute.");
        }

        int A_time = hour*100 + minute;

        for (int i = 0; i < filesize; i++) {
            if (youbimap.get(Day).equals(youbimap.get(days[i]))) {
                if (opentime[i] <= A_time) {
                    if (closetime[i] >= A_time) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}