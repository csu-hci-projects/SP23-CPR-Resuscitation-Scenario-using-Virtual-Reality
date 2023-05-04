using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using Scripts;

public class DisplayResults : MonoBehaviour
{
    public Text textResults;

    public void Start()
    {
        double totalQuestions = 15.0;
        double PCPre = 0.0;
        double PCPost = 0.0;
        PCPre = DataProcess.num_correct_pre / totalQuestions * 100.0;
        PCPost = DataProcess.num_correct_post / totalQuestions * 100.0;

        string PCPreFormatted = PCPre.ToString("F2");
        string PCPostFormatted = PCPost.ToString("F2");

        string PreTest = "Pre Assessment Performance: ";
        string PostTest = "Post Assessment Performance: ";

        textResults.text = PreTest + PCPreFormatted + "%\n" + PostTest + PCPostFormatted + "%";
    }
}