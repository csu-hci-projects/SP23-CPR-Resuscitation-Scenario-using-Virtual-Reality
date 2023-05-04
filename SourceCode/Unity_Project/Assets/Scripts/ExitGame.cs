using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.XR;
using UnityEngine.UI;

public class EndMenu : MonoBehaviour
{
    public void exitgame()
    {
        Debug.Log($"Exiting Game...");
        Application.Quit();

    }
}