using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Video;

public class PlayButton : MonoBehaviour
{
    public VideoPlayer videoPlayer;
    private bool videoWasPlayed = false;
    public GameObject button;

    void Update()
    {
        if (videoPlayer.isPlaying && !videoWasPlayed)
        {
            videoWasPlayed = true;
        }
        else if (!videoPlayer.isPlaying && videoWasPlayed)
        {
            button.SetActive(true);
        }
    }

    public void PlayVideo()
    {
        videoWasPlayed = true;
        videoPlayer.Play();

    }

}