using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DataManager : MonoBehaviour
{
    public static DataManager Instance;

    public string age;
    public string gender;
    public string education;
    public string VRScale;
    public string CPRScale;

    public string q1_pre;
    public string q2_pre;
    public string q3_pre;
    public string q4_pre;
    public string q5_pre;
    public string q6_pre;
    public string q7_pre;
    public string q8_pre;
    public string q9_pre;
    public string q10_pre;
    public string q11_pre;
    public string q12_pre;
    public string q13_pre;
    public string q14_pre;
    public string q15_pre;

    public string PostCPR;
    public string PostEXP;
    public string PostFeed;


    public string q1_post;
    public string q2_post;
    public string q3_post;
    public string q4_post;
    public string q5_post;
    public string q6_post;
    public string q7_post;
    public string q8_post;
    public string q9_post;
    public string q10_post;
    public string q11_post;
    public string q12_post;
    public string q13_post;
    public string q14_post;
    public string q15_post;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }
}