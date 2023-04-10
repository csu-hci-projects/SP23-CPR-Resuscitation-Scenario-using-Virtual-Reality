using System.Collections;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using UnityEngine.Networking;

public class DataProcess : MonoBehaviour
{
    public ToggleGroup currentQuestionToggleGroup;
    public int currentSceneIndex;

    private string URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSeWdPtTo1KhjPYkowJ2hlh_TgT1s_UXyg_tfIl89WdwCd0H-A/formResponse";

    public void Next()
    {
        string answer = currentQuestionToggleGroup.GetFirstActiveToggle().name;
        if (currentSceneIndex >= 2 && currentSceneIndex <= 6)
        {
            switch (currentSceneIndex)
            {
                case 2:
                    DataManager.Instance.age = answer;
                    break;
                case 3:
                    DataManager.Instance.gender = answer;
                    break;
                case 4:
                    DataManager.Instance.education = answer;
                    break;
                case 5:
                    DataManager.Instance.VRScale = answer;
                    break;
                case 6:
                    DataManager.Instance.CPRScale = answer;
                    break;
            }
        }
        else if (currentSceneIndex >= 8 && currentSceneIndex <= 22)
        {
            switch (currentSceneIndex)
            {
                case 8:
                    DataManager.Instance.q1_pre = answer;
                    break;
                case 9:
                    DataManager.Instance.q2_pre = answer;
                    break;
                case 10:
                    DataManager.Instance.q3_pre = answer;
                    break;
                case 11:
                    DataManager.Instance.q4_pre = answer;
                    break;
                case 12:
                    DataManager.Instance.q5_pre = answer;
                    break;
                case 13:
                    DataManager.Instance.q6_pre = answer;
                    break;
                case 14:
                    DataManager.Instance.q7_pre = answer;
                    break;
                case 15:
                    DataManager.Instance.q8_pre = answer;
                    break;
                case 16:
                    DataManager.Instance.q9_pre = answer;
                    break;
                case 17:
                    DataManager.Instance.q10_pre = answer;
                    break;
                case 18:
                    DataManager.Instance.q11_pre = answer;
                    break;
                case 19:
                    DataManager.Instance.q12_pre = answer;
                    break;
                case 20:
                    DataManager.Instance.q13_pre = answer;
                    break;
                case 21:
                    DataManager.Instance.q14_pre = answer;
                    break;
                case 22:
                    DataManager.Instance.q15_pre = answer;
                    break;
            }
        }
        else if (currentSceneIndex >= 25 && currentSceneIndex <= 27)
        {
            switch (currentSceneIndex)
            {
                case 25:
                    DataManager.Instance.PostCPR = answer;
                    break;
                case 26:
                    DataManager.Instance.PostEXP = answer;
                    break;
                case 27:
                    DataManager.Instance.PostFeed = answer;
                    break;
            }
        }

        else if (currentSceneIndex >= 29 && currentSceneIndex <= 43)
        {
            switch (currentSceneIndex)
            {
                case 29:
                    DataManager.Instance.q1_post = answer;
                    break;
                case 30:
                    DataManager.Instance.q2_post = answer;
                    break;
                case 31:
                    DataManager.Instance.q3_post = answer;
                    break;
                case 32:
                    DataManager.Instance.q4_post = answer;
                    break;
                case 33:
                    DataManager.Instance.q5_post = answer;
                    break;
                case 34:
                    DataManager.Instance.q6_post = answer;
                    break;
                case 35:
                    DataManager.Instance.q7_post = answer;
                    break;
                case 36:
                    DataManager.Instance.q8_post = answer;
                    break;
                case 37:
                    DataManager.Instance.q9_post = answer;
                    break;
                case 38:
                    DataManager.Instance.q10_post = answer;
                    break;
                case 39:
                    DataManager.Instance.q11_post = answer;
                    break;
                case 40:
                    DataManager.Instance.q12_post = answer;
                    break;
                case 41:
                    DataManager.Instance.q13_post = answer;
                    break;
                case 42:
                    DataManager.Instance.q14_post = answer;
                    break;
                case 43:
                    DataManager.Instance.q15_post = answer;
                    break;
            }
        }

        else
        {
            Debug.LogError("Invalid scene index");
        }
            if (currentSceneIndex <= 43)
        {
            SceneManager.LoadScene(currentSceneIndex + 1);
        }
    }

    public void Submit()
    {
        StartCoroutine(Post(DataManager.Instance.age, DataManager.Instance.gender, DataManager.Instance.education, DataManager.Instance.VRScale, DataManager.Instance.CPRScale, DataManager.Instance.q1_pre, 
            DataManager.Instance.q2_pre, DataManager.Instance.q3_pre, DataManager.Instance.q4_pre, DataManager.Instance.q5_pre, DataManager.Instance.q6_pre, 
            DataManager.Instance.q7_pre, DataManager.Instance.q8_pre, DataManager.Instance.q9_pre, DataManager.Instance.q10_pre, DataManager.Instance.q11_pre, 
            DataManager.Instance.q12_pre, DataManager.Instance.q13_pre, DataManager.Instance.q14_pre, DataManager.Instance.q15_pre,
            DataManager.Instance.PostFeed, DataManager.Instance.PostEXP, DataManager.Instance.PostCPR, DataManager.Instance.q1_post,
            DataManager.Instance.q2_post, DataManager.Instance.q3_post, DataManager.Instance.q4_post, DataManager.Instance.q5_post, DataManager.Instance.q6_post,
            DataManager.Instance.q7_post, DataManager.Instance.q8_post, DataManager.Instance.q9_post, DataManager.Instance.q10_post, DataManager.Instance.q11_post,
            DataManager.Instance.q12_post, DataManager.Instance.q13_post, DataManager.Instance.q14_post, DataManager.Instance.q15_post));

        Debug.Log(DataManager.Instance.age + " " + DataManager.Instance.gender + " " + DataManager.Instance.education + " " + DataManager.Instance.VRScale + " " + DataManager.Instance.CPRScale);
    }

    IEnumerator Post(string Age, string Gender, string Education, string vrscale, string cprscale,
        string Q1Pre, string Q2Pre, string Q3Pre, string Q4Pre, string Q5Pre, string Q6Pre, string Q7Pre,
        string Q8Pre, string Q9Pre, string Q10Pre, string Q11Pre, string Q12Pre, string Q13Pre, string Q14Pre, string Q15Pre
        ,string postcpr, string postexp, string postfeed, string Q1Post, string Q2Post, string Q3Post, string Q4Post, string Q5Post, string Q6Post, string Q7Post,
        string Q8Post, string Q9Post, string Q10Post, string Q11Post, string Q12Post, string Q13Post, string Q14Post, string Q15Post)
    {
        Debug.Log("Post started");
        WWWForm form = new WWWForm();

        form.AddField("entry.156737009", Age);
        form.AddField("entry.195872643", Gender);
        form.AddField("entry.1034252165", Education);
        form.AddField("entry.542426980", vrscale);
        form.AddField("entry.1693022796", cprscale);

        form.AddField("entry.1405516163", Q1Pre);
        form.AddField("entry.158656312", Q2Pre);
        form.AddField("entry.973847983", Q3Pre);
        form.AddField("entry.41424931", Q4Pre);
        form.AddField("entry.1711354372", Q5Pre);

        form.AddField("entry.930792526", Q6Pre);
        form.AddField("entry.226064971", Q7Pre);
        form.AddField("entry.2067780752", Q8Pre);
        form.AddField("entry.343842086", Q9Pre);
        form.AddField("entry.1094266948", Q10Pre);

        form.AddField("entry.1111429067", Q11Pre);
        form.AddField("entry.1061585106", Q12Pre);
        form.AddField("entry.609129124", Q13Pre);
        form.AddField("entry.1418389755", Q14Pre);
        form.AddField("entry.180310509", Q15Pre);

        form.AddField("entry.913333358", postcpr); 
        form.AddField("entry.1139344393", postexp);
        form.AddField("entry.1135938561", postfeed);

        form.AddField("entry.996745426", Q1Post);
        form.AddField("entry.2001107243", Q2Post);
        form.AddField("entry.121973240", Q3Post);
        form.AddField("entry.425320776", Q4Post);
        form.AddField("entry.1202878326", Q5Post);

        form.AddField("entry.1472025864", Q6Post);
        form.AddField("entry.563404320", Q7Post);
        form.AddField("entry.1709186748", Q8Post);
        form.AddField("entry.2021633485", Q9Post);
        form.AddField("entry.1225991456", Q10Post);

        form.AddField("entry.1390344128", Q11Post);
        form.AddField("entry.1783096688", Q12Post);
        form.AddField("entry.511189549", Q13Post);
        form.AddField("entry.2057623834", Q14Post);
        form.AddField("entry.1687503832", Q15Post);

        /*
        930792526
            226064971
            2067780752
            343842086
            1094266948

            1111429067
            1061585106
            609129124
            1418389755
            180310509

            1135938561
            1139344393
            913333358

            996745426
            2001107243
            121973240
            425320776
            1202878326

        1472025864
        1472025864
        563404320
        563404320
        1709186748
        1709186748
        2021633485
        1225991456

        1390344128
        1783096688
        511189549
        2057623834
        1687503832
            */
        UnityWebRequest www = UnityWebRequest.Post(URL, form);
        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success)
        {
            Debug.Log(www.error);
        }
        else
        {
            Debug.Log("Form submission complete");
        }
    }
}


