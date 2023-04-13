using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using Scripts;


public class SceneSwitcher : MonoBehaviour
{
    private int currentSceneIndex; 
    private string pid;


   public void Next()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
    }

    public void Back()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 1);
    }

    public void Again()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }

    public void RestartAll()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 7);
    }

    public void Divert()
    {
        string pid = DataProcess.participantGroupNumber;
        Debug.Log("The value of pid is: " + pid);

        if (pid == "0") {
            Debug.Log("The value of pid is 0");
            SceneManager.LoadScene(33);
        } else {
            Debug.Log("The value of pid is NOT 0");
            SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
        }
    }

    public void Converge()
    {
        SceneManager.LoadScene(36);
    }

    public void Quit()
    {
        Application.Quit();
    }
}
