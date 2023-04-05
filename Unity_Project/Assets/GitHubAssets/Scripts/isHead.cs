using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;


public class isHead : MonoBehaviour
{
    private bool isMoving = false;

    public Rigidbody rb;
    public Vector3 rbVelocity;

void Start() {
  rb = GetComponent<Rigidbody>();
}
 
void FixedUpdate ()
{
    rbVelocity = rb.velocity;
    if (isMoving && rbVelocity == Vector3.zero)
    {
        //rb has stopped moving
        isMoving = false;
        freezePosition();
    }
    else if (!isMoving && rbVelocity != Vector3.zero)
    {
        isMoving = true;
    }
}

public void freezePosition() {
    Debug.Log(rb + " Freezing Positions");
    rb.constraints = RigidbodyConstraints.FreezePosition;
}

}

