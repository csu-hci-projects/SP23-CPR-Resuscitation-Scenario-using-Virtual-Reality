using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using Scripts;

public class SceneSwitcher : MonoBehaviour
{
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

    public void Divert()
    {
        string pid = DataProcess.participantGroupNumber;
        Debug.Log("The value of pid is: " + pid);

        if (pid == "0")
            SceneManager.LoadScene(33);
        else
            SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
    }

    public void Converge()
    {
        SceneManager.LoadScene(36);
    }
}
